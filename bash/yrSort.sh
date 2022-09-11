for f in *.pdf
do
    subdir=${f//[^0-9]/}
    [ ! -d "$subdir" ] && mkdir -- "$subdir"
    mv "$f" "$subdir"
done
echo "Files sorted successfully"