package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	// var co2, lines uint64
	var lines uint64

	var one_counts []uint
	var consider []string

	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		line := scanner.Text()

		one_counts = make([]uint, len(line))

		for i, c := range line {
			if c == '1' {
				one_counts[i]++
			}
		}

		consider = append(consider, line)
		lines++
	}

	for i, count := range one_counts {
		fmt.Printf("%v\n", consider)
		fmt.Printf("%v\n", one_counts)
		var new_consider []string
		var most_common byte

		if len(consider) == 1 {
			ox, err := strconv.ParseUint(consider[0], 2, 64)
			if err != nil {
				panic(err)
			}

			println(ox)
			break
		}

		if count >= uint(len(consider)/2) {
			most_common = '1'
		} else {
			most_common = '0'
		}

		for _, line := range consider {
			println(line)
			if line[i] == most_common {
				new_consider = append(new_consider, line)
			}
		}

		consider = new_consider
		println()
	}

}
