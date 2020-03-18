echo "First arg: $1"

if [ $1 == 'enter' ]
then
source activate tensorflow_p36
else
source deactivate
fi