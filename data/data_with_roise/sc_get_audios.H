i=0
for entry in `ls *.wav`; do
    python get_voice.py $entry "_${entry}" &
    let i=i+1
    if [ $i -ge 2 ]; then
    wait
    let i=0
    fi
done
