#! /bin/bash

BASE_DIR="plots"

OUTPUT_FOLDER=""
function get_output_folder {
    d=`date +"%y%m%d"`

    it=0
    while [ $it -lt 99 ]; do
        p=$(printf '%s_%02d' "${d}" ${it})
        if [ ! -d "$BASE_DIR/$p" ]; then
            OUTPUT_FOLDER="$p"
            return
        fi

        let it+=1
    done

    echo "Cannot find a valid output folder"
    exit 1
}

get_output_folder

mkdir "$BASE_DIR/$OUTPUT_FOLDER"

#for flavor in MuMu; do
for flavor in MuMu ElEl MuEl ElMu; do
    mkdir "$BASE_DIR/$OUTPUT_FOLDER/$flavor"

    cp TT_plots_base.yml TT_plots_$flavor.yml
    sed "s/base/$flavor/g" -i TT_plots_$flavor.yml
    ../../plotIt/plotIt TT_config_${flavor}.yml -o "$BASE_DIR/$OUTPUT_FOLDER/$flavor"

    # do the yields
    cp TT_yields_base.yml TT_yields_$flavor.yml
    sed "s/base/$flavor/g" -i TT_yields_$flavor.yml
    sed "s/TT_plots/TT_yields/g" -i TT_config_$flavor.yml
    ../../plotIt/plotIt -y -p TT_config_${flavor}.yml -o "$BASE_DIR/$OUTPUT_FOLDER/$flavor"
    sed "s/TT_yields/TT_plots/g" -i TT_config_$flavor.yml
done

for flavor in MuMu ElEl; do
    mkdir "$BASE_DIR/$OUTPUT_FOLDER/${flavor}_ZVeto"

    cp TT_plots_base.yml TT_plots_$flavor.yml
    sed "s/base/${flavor}_ZVeto/g" -i TT_plots_$flavor.yml
    ../../plotIt/plotIt TT_config_${flavor}.yml -o "$BASE_DIR/$OUTPUT_FOLDER/${flavor}_ZVeto"
done

echo ""
echo "Plots saved in $BASE_DIR/$OUTPUT_FOLDER"
