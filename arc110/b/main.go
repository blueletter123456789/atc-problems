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
	t := StrStdin()
	if n == 1 {
		if t == "1" {
			fmt.Println(2 * pow10(10, 10))
		} else {
			fmt.Println(pow10(10, 10))
		}
		return
	}

	si := [3]string{"1", "1", "0"}
	var g int
	if string(t[0]) == "0" {
		g = 2
	} else if string(t[1]) == "0" {
		g = 1
	}

	for i := 0; i < n; i++ {
		if string(t[i]) != si[(i+g)%3] {
			fmt.Println(0)
			return
		}
	}

	ans := (n + g - 1) / 3
	fmt.Println(pow10(10, 10)-ans)

	// Corresponding characters at the end
	// If 1: 10^10 - K (K is numer of 0)
	// If 0: 10^10 - K + 1
}

func NumStdin() int {
	num, err := strconv.Atoi(StrStdin())
	if err != nil {
		panic(err)
	}
	return num
}

func StrStdin() string {
	scan.Scan()
	return scan.Text()
}

func pow10(a, r int) int {
	ret := 1
	for i := 1; i <= r; i++ {
		ret *= a
	}
	return ret
}
