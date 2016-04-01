#pragma once

#define _USE_MATH_DEFINES
#include <cmath>
#include <string>

#include <Math/Vector4D.h>
#include <TH2.h>
#include <TH1.h>
#include <TFile.h>

class SmearingFunction {
  public:
    
    SmearingFunction() {}
    virtual ~SmearingFunction() {}

    virtual double Evaluate(const myLorentzVector& input, myLorentzVector& output, const double psPoint) const { return 0;}
    virtual double Evaluate(double& output, const double psPoint) const { return 0; }

};


class DiracDelta: public SmearingFunction {

  public:

    DiracDelta() {}
    DiracDelta(double value): value(value) {}
    virtual ~DiracDelta() {}

    virtual double Evaluate(const myLorentzVector& input, myLorentzVector& output, const double psPoint) const {
      output = input;
      return 1;
    }
    
    virtual double Evaluate(double& output, const double psPoint) const {
      output = value;
      return 1;
    }

  private:

    double value;
};


class SimpleGaussianOnEnergy: public SmearingFunction {

  public:

    // stdDev is s.t. the standard deviation of the gaussian = Egen*stdDev
    // range is s.t. Egen is generated over an interval of length 2*Ereco*stdDev*range
    SimpleGaussianOnEnergy(const double mean, const double stdDev, const double range):
      mean(mean), stdDev(stdDev), range(range)
      {}
    virtual ~SimpleGaussianOnEnergy() {}

    virtual double Evaluate(const myLorentzVector& input, myLorentzVector& output, const double psPoint) const {
      double Egen = input.E() - range*stdDev*input.E() + 2*range*stdDev*input.E()*psPoint;
      const double pTgen = sqrt( pow(Egen, 2) - pow(input.M(), 2) ) / cosh(input.Eta());
      output.SetCoordinates(pTgen, input.Eta(), input.Phi(), Egen);
      
      return exp( -pow(mean - (input.E()-Egen), 2)/(2*pow(stdDev*Egen, 2)) ) / sqrt(2*M_PI) / (stdDev*Egen);
    }
    
  private:
    
    double mean, stdDev, range;

};


class BreitWigner: public SmearingFunction {

  public:

    BreitWigner(const double mass, const double width, const double range):
      mass(mass), width(width), range(range)
    {
      if(width*range >= mass)
        std::cout << "Warning: Breit-Wigner is only physical near the resonance." << std::endl;
    }
    
    virtual double Evaluate(double &output, const double psPoint) const {
      const double s = -range*width + 2*range*width*psPoint; 

      const double gamma = sqrt( pow(mass, 2) * (pow(mass, 2) + pow(width, 2)));
      const double k = 2*sqrt(2)*mass*width*gamma/(M_PI*sqrt(pow(mass, 2) + gamma));

      return k/(pow(s - pow(mass, 2), 2) + pow(mass*width, 2));
    }

  private:

    double mass, width, range;
};


class Binned1DTransferFunction: public SmearingFunction {
  public:

    Binned1DTransferFunction(const std::string histName, TFile* file, double offset=0): _offset(offset) {
      _TF = dynamic_cast<TH1D*>( file->Get(histName.c_str()) );
      if(!_TF){
        std::cerr << "Error when defining 1D binned TF: unable to retrieve " << histName << " from file " << file->GetPath() << ".\n";
        exit(1);
      }
      _TF->SetDirectory(0);

      std::cout << "Creating 1D TF from histogram " << histName << ".\n";

      _min = _TF->GetXaxis()->GetXmin();
      _max = _TF->GetXaxis()->GetXmax();
      _range = _max - _min; 
 
      std::cout << "Delta range is " << _range << ", min. and max. values are " << _min << ", " << _max << std::endl << std::endl;
    }
 
    virtual ~Binned1DTransferFunction(){
      delete _TF; _TF = nullptr;
    }
    
    virtual double Evaluate(double &output, const double psPoint) const {
      output = _min + _range*psPoint;
      const int bin = _TF->FindFixBin(output);
      output += _offset;
      return _TF->GetBinContent(bin);
    }

  private:

    double _min, _max, _range, _offset;
    TH1D* _TF;
};


class Binned2DTransferFunction: public SmearingFunction {
  
  public:

    Binned2DTransferFunction(const std::string histName, TFile* file){
      _TF = dynamic_cast<TH2F*>( file->Get(histName.c_str()) );
      if(!_TF){
        std::cerr << "Error when defining 2D binned TF: unable to retrieve " << histName << " from file " << file->GetPath() << ".\n";
        exit(1);
      }
      _TF->SetDirectory(0);

      std::cout << "Creating 2D TF from histogram " << histName << ".\n";

      _deltaMin = _TF->GetYaxis()->GetXmin();
      _deltaMax = _TF->GetYaxis()->GetXmax();
      _deltaRange = _deltaMax - _deltaMin; 
      _EgenMax = _TF->GetXaxis()->GetXmax();
      _EgenMin = _TF->GetXaxis()->GetXmin();
 
      std::cout << "Delta range is " << _deltaRange << ", min. and max. values are " << _EgenMin << ", " <<_EgenMax << std::endl << std::endl;
    }
 
    virtual ~Binned2DTransferFunction(){
      delete _TF; _TF = nullptr;
    }
    
    virtual double Evaluate(const myLorentzVector& input, myLorentzVector& output, const double psPoint) const {
      const double Erec = input.E();
      const double Erange = GetDeltaRange(Erec);
      double Egen = Erec - GetDeltaMax(Erec) + Erange * psPoint;
      const double pTgen = sqrt( pow(Egen, 2) - pow(input.M(), 2) ) / cosh(input.Eta());
      output.SetCoordinates(pTgen, input.Eta(), input.Phi(), Egen);
      
      const double delta = Erec - Egen;
      if(Egen < _EgenMin || delta > _deltaMax || delta < _deltaMin)
        return 0.;
      // We assume the TF continues asymptotically as a constant for Egen -> infinity
      if(Egen >= _EgenMax)
        Egen = _EgenMax - 1;

      // Use ROOT's global bin number "feature" for 2-dimensional histograms
      const int bin = _TF->FindFixBin(Egen, delta);
      return _TF->GetBinContent(bin);
    }
    
    double GetDeltaRange(const double &Erec) const {
      return GetDeltaMax(Erec) - GetDeltaMin(Erec);
    }

    double GetDeltaMin(const double &Erec) const {
      return std::max(_deltaMin, Erec - _EgenMax);
    }

    double GetDeltaMax(const double &Erec) const {
      return std::min(_deltaMax, Erec - _EgenMin);
    }
    
  private:

    double _deltaMin, _deltaMax, _deltaRange;
    double _EgenMax, _EgenMin;
    TH2F* _TF;
};
