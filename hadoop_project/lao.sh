# This one uploads a file to the input directory on the HDFS.
# I'm assuming that it's from wherever we decide to save it in our repo
# There's not much direction there
# Also, looking at the text file it seems that there's a line of Bash at the top
# It looks like it might just be the answer???


# Also I'm pretty sure this is how I refer to the parent directory

hdfs dfs -put lao.txt /holbies/input/lao.txt
