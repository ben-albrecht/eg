#/bin/sh

eval set -- $(getopt -n $0 -o "-rvxl:" -- "$@")

declare r v x l
declare -a files
while [ $# -gt 0 ] ; do
        case "$1" in
                -r) r=1 ; shift ;;
                -v) v=1 ; shift ;;
                -x) x=1 ; shift ;;
                -l) shift ; l="$1" ; shift ;;
                --) shift ;;
                -*) echo "bad option '$1'" ; exit 1 ;;
                *) files=("${files[@]}" "$1") ; shift ;;
         esac
done

if [ ${#files} -eq 0 ] ; then
        echo output file required
        exit 1
fi

[ ! -z "$r" ] && echo "r on"
[ ! -z "$v" ] && echo "v on"
[ ! -z "$x" ] && echo "x on"

[ ! -z "$l" ] && echo "l == $l"

echo "output file(s): ${files[@]}"
