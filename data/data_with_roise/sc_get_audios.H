for entry in `ls`; do
    python get_voice.py $entry "_${entry}"
done