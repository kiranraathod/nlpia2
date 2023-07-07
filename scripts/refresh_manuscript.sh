#!/usr/bin/env bash
# Delete all *.adoc files in nlpia2/data/manuscript/adoc 
# and replaces with hard links from nlpia-manuscript/manuscript/adoc/

# FIXME: gitlab doesn't like hard links to unchanged files (prereceive hook)
# TODO: make this a for loop

# rm -f src/nlpia2/data/manuscript/adoc/Chapter*.adoc
# git commit -am 'rm Chapter*'
ln -f ../../nlpia-manuscript/manuscript/adoc/Chapter*.adoc src/nlpia2/data/manuscript/adoc/
# git commit -am 'hard link Chapter*'

# rm -f src/nlpia2/data/manuscript/adoc/Appendix*.adoc
# git commit -am 'rm Appendix*'
ln -f ../../nlpia-manuscript/manuscript/adoc/Appendix*.adoc src/nlpia2/data/manuscript/adoc/
# git commit -am 'hard link Appendix*'

ln -f ../../nlpia-manuscript/manuscript/adoc/TOC* src/nlpia2/data/manuscript/adoc/
ln -f ../../nlpia-manuscript/manuscript/adoc/outline* src/nlpia2/data/manuscript/adoc/

# rm -f src/nlpia2/data/manuscript/adoc/Glossary.adoc
# git commit -am 'rm Glossary.adoc'
ln -f ../../nlpia-manuscript/manuscript/adoc/Glossary.adoc src/nlpia2/data/manuscript/adoc/
# git commit -am 'hard link Glossary.adoc'

