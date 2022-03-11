#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Luminescence
Version  : 0.9.19
Release  : 49
URL      : https://cran.r-project.org/src/contrib/Luminescence_0.9.19.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Luminescence_0.9.19.tar.gz
Summary  : Comprehensive Luminescence Dating Data Analysis
Group    : Development/Tools
License  : GPL-3.0
Requires: R-Luminescence-lib = %{version}-%{release}
Requires: R-DEoptim
Requires: R-Rcpp
Requires: R-RcppArmadillo
Requires: R-XML
Requires: R-bbmle
Requires: R-data.table
Requires: R-httr
Requires: R-lamW
Requires: R-matrixStats
Requires: R-mclust
Requires: R-minpack.lm
Requires: R-plotrix
Requires: R-readxl
Requires: R-shape
Requires: R-zoo
BuildRequires : R-DEoptim
BuildRequires : R-Rcpp
BuildRequires : R-RcppArmadillo
BuildRequires : R-XML
BuildRequires : R-bbmle
BuildRequires : R-data.table
BuildRequires : R-httr
BuildRequires : R-lamW
BuildRequires : R-matrixStats
BuildRequires : R-mclust
BuildRequires : R-minpack.lm
BuildRequires : R-plotrix
BuildRequires : R-readxl
BuildRequires : R-shape
BuildRequires : R-zoo
BuildRequires : buildreq-R

%description
A collection of various R functions for the purpose of Luminescence dating data
analysis. This includes, amongst others, data import, export, application of
age models, curve deconvolution, sequence analysis and plotting of equivalent
dose distributions.

%package lib
Summary: lib components for the R-Luminescence package.
Group: Libraries

%description lib
lib components for the R-Luminescence package.


%prep
%setup -q -c -n Luminescence
cd %{_builddir}/Luminescence

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647017501

%install
export SOURCE_DATE_EPOCH=1647017501
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Luminescence
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Luminescence
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Luminescence
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc Luminescence || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Luminescence/CITATION
/usr/lib64/R/library/Luminescence/DESCRIPTION
/usr/lib64/R/library/Luminescence/INDEX
/usr/lib64/R/library/Luminescence/Meta/Rd.rds
/usr/lib64/R/library/Luminescence/Meta/data.rds
/usr/lib64/R/library/Luminescence/Meta/features.rds
/usr/lib64/R/library/Luminescence/Meta/hsearch.rds
/usr/lib64/R/library/Luminescence/Meta/links.rds
/usr/lib64/R/library/Luminescence/Meta/nsInfo.rds
/usr/lib64/R/library/Luminescence/Meta/package.rds
/usr/lib64/R/library/Luminescence/Meta/vignette.rds
/usr/lib64/R/library/Luminescence/NAMESPACE
/usr/lib64/R/library/Luminescence/NEWS.md
/usr/lib64/R/library/Luminescence/R/Luminescence
/usr/lib64/R/library/Luminescence/R/Luminescence.rdb
/usr/lib64/R/library/Luminescence/R/Luminescence.rdx
/usr/lib64/R/library/Luminescence/WORDLIST
/usr/lib64/R/library/Luminescence/data/BaseDataSet.ConversionFactors.rda
/usr/lib64/R/library/Luminescence/data/BaseDataSet.CosmicDoseRate.rda
/usr/lib64/R/library/Luminescence/data/BaseDataSet.FractionalGammaDose.rda
/usr/lib64/R/library/Luminescence/data/BaseDataSet.GrainSizeAttenuation.rda
/usr/lib64/R/library/Luminescence/data/ExampleData.Al2O3C.rda
/usr/lib64/R/library/Luminescence/data/ExampleData.BINfileData.rda
/usr/lib64/R/library/Luminescence/data/ExampleData.CW_OSL_Curve.rda
/usr/lib64/R/library/Luminescence/data/ExampleData.CobbleData.rda
/usr/lib64/R/library/Luminescence/data/ExampleData.DeValues.rda
/usr/lib64/R/library/Luminescence/data/ExampleData.Fading.rda
/usr/lib64/R/library/Luminescence/data/ExampleData.FittingLM.rda
/usr/lib64/R/library/Luminescence/data/ExampleData.LxTxData.rda
/usr/lib64/R/library/Luminescence/data/ExampleData.LxTxOSLData.rda
/usr/lib64/R/library/Luminescence/data/ExampleData.RLum.Analysis.rda
/usr/lib64/R/library/Luminescence/data/ExampleData.RLum.Data.Image.rda
/usr/lib64/R/library/Luminescence/data/ExampleData.ScaleGammaDose.rda
/usr/lib64/R/library/Luminescence/data/ExampleData.SurfaceExposure.rda
/usr/lib64/R/library/Luminescence/data/ExampleData.TR_OSL.rda
/usr/lib64/R/library/Luminescence/data/ExampleData.XSYG.rda
/usr/lib64/R/library/Luminescence/data/ExampleData.portableOSL.rda
/usr/lib64/R/library/Luminescence/data/datalist
/usr/lib64/R/library/Luminescence/doc/S4classObjects.pdf
/usr/lib64/R/library/Luminescence/doc/S4classObjects.pdf.asis
/usr/lib64/R/library/Luminescence/doc/index.html
/usr/lib64/R/library/Luminescence/extdata/Daybreak_TestFile.DAT
/usr/lib64/R/library/Luminescence/extdata/Daybreak_TestFile.txt
/usr/lib64/R/library/Luminescence/extdata/DorNie_0016.psl
/usr/lib64/R/library/Luminescence/extdata/QNL84_2_bleached.txt
/usr/lib64/R/library/Luminescence/extdata/QNL84_2_unbleached.txt
/usr/lib64/R/library/Luminescence/extdata/RF_file.rf
/usr/lib64/R/library/Luminescence/extdata/STRB87_1_bleached.txt
/usr/lib64/R/library/Luminescence/extdata/STRB87_1_unbleached.txt
/usr/lib64/R/library/Luminescence/extdata/TIFFfile.tif
/usr/lib64/R/library/Luminescence/extdata/XSYG_file.xsyg
/usr/lib64/R/library/Luminescence/help/AnIndex
/usr/lib64/R/library/Luminescence/help/Luminescence.rdb
/usr/lib64/R/library/Luminescence/help/Luminescence.rdx
/usr/lib64/R/library/Luminescence/help/aliases.rds
/usr/lib64/R/library/Luminescence/help/figures/Luminescence_logo.png
/usr/lib64/R/library/Luminescence/help/figures/README-Package_DependencyGraph.png
/usr/lib64/R/library/Luminescence/help/figures/README-Screenshot_AddIn.png
/usr/lib64/R/library/Luminescence/help/paths.rds
/usr/lib64/R/library/Luminescence/html/00Index.html
/usr/lib64/R/library/Luminescence/html/R.css
/usr/lib64/R/library/Luminescence/rstudio/addins.dcf
/usr/lib64/R/library/Luminescence/tests/spelling.R
/usr/lib64/R/library/Luminescence/tests/testthat.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_Analyse_SAROSLdata.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_CW2pX.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_PSL2RisoeBINfiledata.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_RLum.Analysis-class.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_RLum.Data.Curve.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_RLum.Data.Image.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_RLum.Data.Spectrum.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_RLum.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_RisoeBINfileData-class.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_Second2Gray.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_analyse_Al2O3C_CrossTalk.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_analyse_Al2O3C_ITC.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_analyse_Al2O3C_Measurement.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_analyse_FadingMeasurement.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_analyse_IRSARRF.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_analyse_SARCWOSL.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_analyse_SARTL.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_analyse_baSAR.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_analyse_pIRIRSequence.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_analyse_portableOSL.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_apply_CosmicRayRemoval.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_apply_EfficiencyCorrection.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_as_latex_table.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_bin_RLumData.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_calc_AliquotSize.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_calc_AverageDose.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_calc_CentralDose.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_calc_CobbeDoseRate.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_calc_CommonDose.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_calc_CosmicDoseRate.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_calc_FadingCorr.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_calc_FastRatio.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_calc_FiniteMixture.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_calc_FuchsLang2001.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_calc_HomogeneityTest.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_calc_Huntley2008.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_calc_IEU.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_calc_Lamothe2003.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_calc_MaxDose.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_calc_MinDose.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_calc_OSLLxTxRatio.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_calc_SourceDoseRate.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_calc_Statistics.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_calc_TLLxTxRatio.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_calc_ThermalLifetime.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_calc_WodaFuchs2008.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_calc_gSGC.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_calc_gSGC_feldspar.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_combine_De_Dr.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_convert_Activity2Concentration.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_convert_Concentration2DoseRate.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_convert_PSL2CSV.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_convert_RLum2Risoe.BINfileData.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_convert_SG2MG.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_convert_Wavelength2Energy.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_convert_XYSG2CSV.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_extract_IrradiationTimes.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_extract_ROI.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_fit_CWCurve.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_fit_EmissionSpectra.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_fit_LMCurve.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_fit_OSLLifeTimes.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_fit_SurfaceExposure.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_fit_ThermalQuenching.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_get_RLum.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_github.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_internals.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_merge_RLumDataCurve.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_merge_RLumResults.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_merge_RisoeBINfileData.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_methods_DRAC.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_methods_S3.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_names_RLum.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_plot_AbanicoPlot.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_plot_DRCSummary.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_plot_Functions.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_plot_GrowthCurve.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_plot_OSLAgeSummary.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_plot_RLum.Analysis.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_plot_RLum.Data.Curve.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_plot_RLum.Data.Image.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_plot_RLum.Data.Spectrum.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_plot_RLum.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_plot_ROI.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_read_BIN2R.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_read_Daybreak2R.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_read_PSL2R.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_read_RF2R.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_read_SPE2R.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_read_TIFF2R.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_read_XSYG2R.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_replicate_RLum.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_report_RLum.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_scale_GammaDose.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_smooth_RLum.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_structure_RLum.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_subset_RLum.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_template_DRAC.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_use_DRAC.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_verify_SingleGrainData.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_write_R2BIN.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_write_R2TIFF.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_write_RLum2CSV.R
/usr/lib64/R/library/Luminescence/tests/testthat/test_zzz.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/Luminescence/libs/Luminescence.so
/usr/lib64/R/library/Luminescence/libs/Luminescence.so.avx2
/usr/lib64/R/library/Luminescence/libs/Luminescence.so.avx512
