package main

import (
	"bufio"
	"os"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func getDepth(scanner *bufio.Scanner) int {
	scanner.Scan()
	depth, err := strconv.Atoi(scanner.Text())
	check(err)

	return depth
}

func main() {
	count := 0

	scanner := bufio.NewScanner(os.Stdin)

	prevFirst := getDepth(scanner)
	prevSecond := getDepth(scanner)
	prevThird := getDepth(scanner)

	for scanner.Scan() {
		cur, err := strconv.Atoi(scanner.Text())
		check(err)

		if prevFirst < cur {
			count++
		}

		prevFirst = prevSecond
		prevSecond = prevThird
		prevThird = cur
	}

	println(count)
}
