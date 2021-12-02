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
	var x, z int

	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		line := scanner.Text()

		ins := strings.Split(line, " ")

		switch ins[0] {
		case "forward":
			tmp, err := strconv.Atoi(ins[1])
			check(err)

			x += tmp
		case "up":
			tmp, err := strconv.Atoi(ins[1])
			check(err)

			z -= tmp
		case "down":
			tmp, err := strconv.Atoi(ins[1])
			check(err)

			z += tmp
		}
	}

	println(x * z)
}
