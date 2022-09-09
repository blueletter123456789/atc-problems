package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var scan = bufio.NewScanner(os.Stdin)

const (
	initBufSize = 10000
	maxBufSize = 10000000
)

func init() {
	buf := make([]byte, initBufSize)
	scan.Buffer(buf, maxBufSize)
	scan.Split(bufio.ScanWords)
}

func main() {
	n := NumStdin()
	a := NumStdin()
	b := NumStdin()

	var dist int
	for i := 0; i < n; i++ {
		s := ChrStdin()
		d := NumStdin()
		if s == "East" {
			dist += min(max(a, d), b)
		} else {
			dist -= min(max(a, d), b)
		}
	}

	if dist == 0 {
		fmt.Println(dist)
	} else if dist > 0 {
		fmt.Printf("East %d\n", dist)
	} else {
		fmt.Printf("West %d\n", -dist)
	}
}

func ChrStdin() string {
	scan.Scan()
	return scan.Text()
}

func NumStdin() int {
	num, err := strconv.Atoi(ChrStdin())
	if err != nil {
		panic(err)
	}
	return num
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
