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
	_ = NumStdin()
	s := ChrStdin()

	// var ans string
	ans := make([]byte, 0, 300)
	front := make([]byte, 0, 100)
	var cnt int
	for _, chr := range s {
		if string(chr) == "(" {
			cnt++
			// ans += "("
			ans = append(ans, '(')
		} else if cnt > 0 {
			cnt--
			// ans += ")"
			ans = append(ans, ')')
		} else {
			// ans = "(" + ans + ")"
			front = append(front, '(')
			ans = append(ans, ')')
		}
	}

	for cnt > 0 {
		// ans += ")"
		ans = append(ans, ')')
		cnt--
	}

	fmt.Println(string(append(front, ans...)))
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
