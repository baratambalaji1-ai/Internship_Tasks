# Mars Exploration

## Problem Statement

A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.

Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, determine how many letters of the SOS message have been changed by radiation.

## Function Description

Complete the `marsExploration` function.

### Parameter
- `s`: A string representing the signal received on Earth.

### Returns
- An integer representing the number of letters changed during transmission.

## Input Format

There is one line of input containing a single string `s`.

## Constraints

- `s` contains only uppercase English letters (`A-Z`).
- The length of `s` is a multiple of 3.

## Sample Input 0

```text
SOSSPSSQSSOR
```

## Sample Output 0

```text
3
```

## Explanation

The expected signal is:

```text
SOSSOSSOSSOS
```

The received signal is:

```text
SOSSPSSQSSOR
```

Three characters differ from the expected signal, so the answer is `3`.

## Sample Input 1

```text
SOSSOT
```

## Sample Output 1

```text
1
```

## Sample Input 2

```text
SOSSOSSOS
```

## Sample Output 2

```text
0
```
