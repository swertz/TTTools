#pragma once

#define _USE_MATH_DEFINES
#include <cmath>
#include <string>
#include <random>
#include <functional>

#include <Math/VectorUtil.h>
#include <Math/Vector4D.h>
#include <Math/Vector3Dfwd.h>
#include <Math/AxisAngle.h>
#include <TH2.h>
#include <TH1.h>
#include <TFile.h>

#define DELTA_PRECISION_REL 10e-4
#define DELTA_PRECISION_ABS 10e-6

/* 
 * Virtual base class for all smearing functions.
 * Has two calls, and two modes:
 *  -- Modes:
 *      - Unweighted: the solutions returned follow the PDF, the weight returned is 1. Warning: if the efficiency is very low, no check is made that the number of attempts in the unweighting be reasonable!
 *      - Weighted: the solutions returned are uniformly distributed, the weight returned is the PDF evaluated on the solution
 *  -- Calls:
 *      - Vector: an input vector is given, and transformed to give the output vector
 *      - Scalar: either an output scalar is built, or the TF is simply evaluated on an input
 *
 */
class SmearingFunction {
  public:
    
    SmearingFunction(): myPSgen(0, 1) {}
    virtual ~SmearingFunction() {}

    virtual double Evaluate(const myLorentzVector& input, myLorentzVector& output, const bool unweighted = true) { return 0;}
    virtual double Evaluate(double& output, const bool unweighted) { return 0; } // No default value here since it would be ambiguous with this second overload:
    virtual double Evaluate(const double input) { return 0; }
      
    double getRandom() { return myPSgen(engine); }

  private:

    std::mt19937_64 engine;
    std::uniform_real_distribution<double> myPSgen;
};


class DiracDelta: public SmearingFunction {

  public:

    DiracDelta(): value(0) {}
    DiracDelta(double value): value(value) {}
    virtual ~DiracDelta() {}

    virtual double Evaluate(const myLorentzVector& input, myLorentzVector& output, const bool unweighted = true) {
      output = input;
      return 1;
    }
    
    virtual double Evaluate(double& output, const bool unweighted) {
      output = value;
      return 1;
    }

    virtual double Evaluate(const double input) {
      return std::abs(input-value) <= std::max(std::abs(input), std::abs(value))*DELTA_PRECISION_REL && std::abs(input-value) <= DELTA_PRECISION_ABS;
    }

  private:

    double value;
};

// TODO: move the Gaussian to weighted/unweighted evaluation
// ... Gaussian maybe not needed?
/*class SimpleGaussianOnEnergy: public SmearingFunction {

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

};*/


class BreitWigner: public SmearingFunction {

  public:

    BreitWigner(const double mass, const double width, const double range):
      mass(mass), width(width), range(range),
      gamma( sqrt( pow(mass, 2) * (pow(mass, 2) + pow(width, 2))) ), 
      k( 2*sqrt(2)*mass*width*gamma/(M_PI*sqrt(pow(mass, 2) + gamma)) )
    {
      if(width*range >= mass)
        std::cout << "Warning: Breit-Wigner is only physical near the resonance." << std::endl;
    }

    virtual ~BreitWigner() {};
    
    virtual double Evaluate(double &output, bool unweighted) {

      if(unweighted) {
        
        const double max = BW(mass);
        
        do {
          output = toRange(getRandom());
        } while(BW(output) > getRandom()*max);
        
        return 1;
      
      } else {
        
        output = toRange(getRandom());
        return BW(output);
      
      }
    
    }

    virtual double Evaluate(const double input) {
      if(input < 0)
        return 0;
      return BW(input); 
    }

  private:

    const double mass, width, range, gamma, k;
    
    double toRange(const double psPoint) const {
      return -range*width + 2*range*width*psPoint;
    }
    
    double BW(const double sqrts) const {
      return k/(pow(pow(sqrts, 2) - pow(mass, 2), 2) + pow(mass*width, 2));
    }
};


class Binned1DTransferFunction: public SmearingFunction {
  public:

    Binned1DTransferFunction(const std::string histName, TFile* file, double offset=0): _offset(offset) {
      _TF = dynamic_cast<TH1F*>( file->Get(histName.c_str()) );
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
    
    virtual double Evaluate(double &output, const bool unweighted) {
      uint32_t bin;
     
      if(unweighted) {
        
        const double max = _TF->GetMaximum();
        
        do {
          
          output = _min + _range*getRandom();
          bin = _TF->FindFixBin(output);
        
        } while(_TF->GetBinContent(bin) < getRandom()*max);
        
        output += _offset;
        return 1;
      
      } else {
        
        output = _min + _range*getRandom();
        bin = _TF->FindFixBin(output);
        output += _offset;
        
        return _TF->GetBinContent(bin);
      
      }
    
    }
    
    virtual double Evaluate(const double input) {
      if(input < _min || input >= _max)
        return 0;
      const uint32_t bin = _TF->FindFixBin(input - _offset);
      return _TF->GetBinContent(bin);
    }

  private:

    double _min, _max, _range, _offset;
    TH1F* _TF;
};

class Binned1DTransferFunctionOnEnergyRatio: public Binned1DTransferFunction {
  public:  
    
    Binned1DTransferFunctionOnEnergyRatio(const std::string histName, TFile* file): 
      Binned1DTransferFunction(histName, file) {}
    
    virtual ~Binned1DTransferFunctionOnEnergyRatio() {};

    virtual double Evaluate(const myLorentzVector& input, myLorentzVector& output, const bool unweighted = true) {
      
      double chosenRatio;
      const double weight = Binned1DTransferFunction::Evaluate(chosenRatio, unweighted);
      
      const double Egen = chosenRatio*input.E();
      const double pTgen = sqrt( pow(Egen, 2) - pow(input.M(), 2) ) / cosh(input.Eta());
      output.SetCoordinates(pTgen, input.Eta(), input.Phi(), Egen);
      
      return weight;
    }
};


// Rotate by an angle distributed as the PDF histogram, along a random direction
class Binned1DTransferFunctionOnAngle: public Binned1DTransferFunction {
  
  using XYZVector = ROOT::Math::XYZVector;
  using AxisAngle = ROOT::Math::AxisAngle;

  public:  
    
    Binned1DTransferFunctionOnAngle(const std::string histName, TFile* file): 
      Binned1DTransferFunction(histName, file) {}
    
    virtual ~Binned1DTransferFunctionOnAngle() {};

    virtual double Evaluate(const myLorentzVector& input, myLorentzVector& output, const bool unweighted = true) {
      // To get the axis describing the direction, first rotate the original vector by 90° (along any axis),
      // then rotate this by an random angle (uniformly distributed) around the origin vector.
      // Finally, get an angle distributed as the PDF, and rotate the 4-vector by this angle along the direction found above.
      
      XYZVector origDir(input.Vect());
      XYZVector tempAxis = ROOT::Math::VectorUtil::RotateX(origDir, M_PI/2);
      AxisAngle rotAlongOrigDir(origDir, getRandom()*2*M_PI);
      XYZVector axis = rotAlongOrigDir(tempAxis);
      
      double angle;
      const double weight = Binned1DTransferFunction::Evaluate(angle, unweighted);
      
      AxisAngle rotAlongAxis(axis, angle);
      output = rotAlongAxis(input);
      
      return weight; 
    }
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
    
    virtual double Evaluate(const myLorentzVector& input, myLorentzVector& output, const double psPoint) {
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
