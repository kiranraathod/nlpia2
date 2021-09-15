egrep -h '^[=]+ ' manuscript/adoc/Chapter*.adoc > docs/headings.adoc
sed 's/=/#/g' docs/headings.adoc > docs/headings.md
sed 's/==== /      * /g' docs/headings.adoc > docs/outline.md
sed -i 's/=== /    * /g' docs/outline.md
sed -i 's/== /  * /g' docs/outline.md
sed -i 's/= /* /g' docs/outline.md
# rm -f headings.adoc

# pandoc --atx-headers     --verbose     --wrap=none     --toc     --reference-links     -s -o outline.adoc     outline.md


