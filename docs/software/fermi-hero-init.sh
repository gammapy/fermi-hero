# This is an example init file ... you'll have to adapt the PATHs / versions to your system
#
export FERMI_HERO = /Users/deil/FERMI_HERO

export HEADAS=$FERMI_HERO
source $HEADAS/headas-init.sh

export FERMI_DIR=$FERMI_HERO/ScienceTools-v9r31p1-fssc-20130410-x86_64-apple-darwin12.2.0/x86_64-apple-darwin12.2.0
source $FERMI_DIR/fermi-init.sh

export ENRICO_DIR=$FERMI_HERO/enrico
source $ENRICO_DIR/enrico-init.sh

alias topcat="java -Xms512m -Xmx4024m -jar /Applications/TOPCAT.app/Contents/Resources/Java/topcat-full.jar"
alias aladin="java -Xms512m -Xmx4024m -jar /Applications/Aladin.app/Contents/Resources/Java/Aladin.jar"

# Add location of binaries to your PATH, e.g. for ds9:
export PATH=$PATH:$FERMI_HERO