package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strings"
)

func readBoard(scanner *bufio.Scanner) ([5][5]string, error) {
	var board [5][5]string
	re := regexp.MustCompile(`\s+`)

	scanner.Scan()
	for i := 0; i < 5; i++ {
		if !scanner.Scan() {
			return [5][5]string{}, fmt.Errorf("error reading board")
		}

		for j, c := range re.Split(scanner.Text(), 5) {
			board[i][j] = c
		}
	}

	return board, nil
}

func main() {
	var boards [][5][5]string
	var nums []string

	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()
	line := scanner.Text()
	split := strings.Split(line, ",")

	nums = make([]string, len(split))

	for _, c := range split {
		nums = append(nums, c)
	}

	fmt.Printf("%v\n", nums)
	for {
		board, err := readBoard(scanner)
		if err != nil {
			break
		}

		boards = append(boards, board)
	}

	fmt.Printf("%v\n", boards)

	for _, num := range nums {
		for _, board := range boards {
			for i, c := range board {
				for j, d := range c {
					if d == num {
						board[i][j] = "X"
					}
				}
			}
		}
	}

	fmt.Printf("%v\n", boards)

}
