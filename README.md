# *Violin*

### *Instruction*

*Cello and Eugene requires users to learn Verilog or Eugene languages, making synthetic biology specification less accessible.* 

[Detailed presentation can see here](https://docs.google.com/presentation/d/14_qUHwvXxcquGgrCJRIU8BuG7QFWK47KHGbUoXAWtFU/edit?usp=sharing)



### *Installation*

1. *cd /violin*

2. *pip install -r requirment.txt*

3. *create your own requirement or add libraries, please use*

   *pip freeze > requirement.txt*

4. Chrome Driver Installation
   1. check for chrome version: HELP->ABOUT
   2. download according to chrome version from [Google](https://sites.google.com/chromium.org/driver/downloads?authuser=0)
   3. If you are on windows, please add it to PATH

### RUN(in CMD/cli)

1. pip install --editable .

2. violin(command example)

   1. violin --help

   2. violin startCello --input=pTac --input=pBAD --output=sigmaT7

   3. violin viewTruth

   4. violin viewVerilog

   5. violin createTruthTable

   6. violin compile

   7. ```python
      violin emptyTruthTable
      how many input do you want? [1]: 2
      
      ```



### Logic* Example*

- *negation*: `'not'`, `'-'`, `'~'`
- *logical disjunction*: `'or'`
- *logical nor*: `'nor'`
- *exclusive disjunction*: `'xor'`, `'!='`
- *logical conjunction*: `'and'`
- *logical NAND*: `'nand'`
- *material implication*: `'=>'`, `'implies'`
- *logical biconditional*: `'='`



### *How we approached*

*3/20*

* Study Python’s logic design syntax of specifying genetic construct (Li)Get familiar with Cello (Chen, Wang)*

*4/3*

* Learn how to compile python into Verilog (Wang)Learn how to run the compiled Verilog in Cello (Chen)*

*4/17*

* Find a way to get Cello output into Eugene and return the final design back to user (Chen, Wang)Write test code (Li)*

*4/22 or 4/27*

* (ALL)Complete the Video Prepare presentation*

### *Author*

*This project is for Boston University EC/BE 552* 

*– Computational Synthetic Biology for Engineers -*

*Spring 2021*

*Instructor: Prof. Douglas Densmore (dougd@bu.edu)*

1. *Yaopu Wang*
2. *Yuxuan Chen*
3. *Yiming Li*