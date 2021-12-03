package main

import (
	"bufio"
	"math"
	"os"
)

func main() {
	var gamma, epsilon, lines uint

	var one_counts []uint

	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		line := scanner.Text()

		if one_counts == nil {
			one_counts = make([]uint, len(line))
		}

		for i, c := range line {
			if c == '1' {
				one_counts[i]++
			}
		}

		lines++
	}

	for i, c := range one_counts {
		if c >= lines/2 {
			gamma += uint(math.Pow(2, float64(len(one_counts)-i-1)))
		}
	}

	for i := range one_counts {
		// fmt.Printf("%b\n", gamma&(0b1<<i))
		epsilon += (0b1 << i) ^ (gamma & (0b1 << i))
	}

	println(gamma * epsilon)
}
