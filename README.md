# visualise-suttas
Some scripts for visualising certain relationships between suttas. 

requires installing graphviz in your system then the python graphviz library 

USE: just run the scripts python3 blabla.py see what they do (won't delete your stuff I promise)

TODO:

[1] essentially the same but now do it for Mahijama Nikaya, Digha etc and combine into a single command line app with flags 

[2] instead of outputting an svg or pdf can we use the graphviz file to instead serve to an interactive graph GUI like with d3 in the browser?  e.g. possibly use https://github.com/magjac/d3-graphviz

[3] See what relationships there are and just show 2 or 3 hops from a sutta. 

[4] do it with d3 or the clojurescript equivalent - when it gets big it's going to be hard (there's already a map of suttas this way but what we want to do is visualise parallels or simularities - the goal is I'm just trying to understand enough so that the "edges" of the graph between the "nodes" which are the suttas themselves can be different kinds of relationships. 
