#!/bin/sh
I=0;
while true; do
        if [ -e "$I.mp3" ]; then
                L=""
                for n in `seq $I $((I+100))`; do
                        L="$L $n.mp3"
                done
                mpg123 $L
                I=$((I+1))
        else
                sleep 0.2
        fi
done

