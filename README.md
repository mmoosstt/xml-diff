# XmlXdiff #
 - generating nice plots of differences between xml files
 - general comparison without grammatical information
 - playground for performance analysis
 - principle works
 
# Implementation #
 - creating an hashed tree representation of each element
 - each element is identified by it's xml path and a hash

# Status Quo #

<figure>
	<img src="./lib/XmlXdiff/tests/test1/xdiff_a_b.svg" alt="test1">
</figure>


## To Be Investigated/Implemented
 - xdiff cost rating for moved and deleted leafs
 - gravity spline for moved elements
 - performance analysis and improvements (different hash algorithms, ...)
 - remove lxml path generation for more suitable paths (absolute tag[position]/tag[position]...
 - figure out how to create a general python package
 
# Inspired by xml-diff #
## Compare two XML files in unordered manner #

XML has been used to transfer hierarchical data. 
In most of those cases, the ordered relation between sibling 
nodes not important - only ancestor relation is important.

The [X-Diff](http://pages.cs.wisc.edu/~yuanwang/xdiff.html) algorithm 
describes how two XML documents can be effectively compared in an unordered
manner.

## License ##

TBD

# Tests #

## Overview ##
|test focus|test available|test result|
|---|---|---|
|ElementUnchanged|test5|   |
|ElementAdded|test2|   |
|ElementDeleted|test4|   |
|ElementMoved|test5|   |
|ElementTagConsitency|test3|   |
|ElementTextAttributeValueConsitency|test7|   |
|ElementTagAttributeNameConsitency|test6|   |
|ElementChanged|   |   |
|ElementVerified|   |   |
|ElementUnknown|   |   |   |   |
|ElementWithNamespace|test8|   |   |   |

## Results ##

<figure>
	<img src="./lib/XmlXdiff/tests/test1/xdiff_a_b.svg" alt="test1">
</figure>

<figure>
	<img src="./lib/XmlXdiff/tests/test2/xdiff_a_b.svg" alt="test2">
</figure>

<figure>
	<img src="./lib/XmlXdiff/tests/test3/xdiff_a_b.svg" alt="test3">
</figure>

<figure>
	<img src="./lib/XmlXdiff/tests/test4/xdiff_a_b.svg" alt="test4">
</figure>

<figure>
	<img src="./lib/XmlXdiff/tests/test5/xdiff_a_b.svg" alt="test5">
</figure>

<figure>
	<img src="./lib/XmlXdiff/tests/test6/xdiff_a_b.svg" alt="test6">
</figure>

<figure>
	<img src="./lib/XmlXdiff/tests/test7/xdiff_a_b.svg" alt="test7">
</figure>

<figure>
	<img src="./lib/XmlXdiff/tests/test8/xdiff_a_b.svg" alt="test8">
</figure>

<figure>
	<img src="./lib/XmlXdiff/tests/test9/xdiff_a_b.svg" alt="test9">
</figure>

