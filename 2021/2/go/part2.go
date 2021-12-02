package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	var x, z, aim int

	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		line := scanner.Text()

		ins := strings.Split(line, " ")

		switch ins[0] {
		case "forward":
			tmp, err := strconv.Atoi(ins[1])
			check(err)

			x += tmp
			z += aim * tmp
		case "up":
			tmp, err := strconv.Atoi(ins[1])
			check(err)
			aim -= tmp
		case "down":
			tmp, err := strconv.Atoi(ins[1])
			check(err)
			aim += tmp
		}
	}

	println(x * z)
}
