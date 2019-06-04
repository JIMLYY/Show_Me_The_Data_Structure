## Description for Problem 3: Huffman Coding
A __Huffman code__ is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.

The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each character. The Huffman code can be of any length and does not require a prefix; therefore, this binary code can be visualized on a binary tree with each encoded character being stored on leafs.

There are many types of pseudocode for this algorithm. At the basic core, it is comprised of building a Huffman tree, encoding the data, and, lastly, decoding the data.

* Here is one type of pseudocode for this coding schema:
* Build and sort a list of tuples from lowest to highest frequencies.<br>
* Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)<br>
* Trim the Huffman Tree (remove the frequencies from the previously built tree).<br>
* Encode the text into its compressed form.<br>
* Decode the text from its compressed form.<br>

You then will need to create encoding, decoding, and sizing schemas.<br>
### Resources:
[Huffman Visualization!](https://people.ok.ubc.ca/ylucet/DS/Huffman.html)<br>
[Tree Generator](http://huffman.ooz.ie/)<br>
[Additional Explanation](https://www.siggraph.org/education/materials/HyperGraph/video/mpeg/mpegfaq/huffman_tutorial.html)
