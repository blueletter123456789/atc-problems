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
	s := StrStdin()
	var ans int
	for i := 1; i < n-1; i++ {
		words := make(map[string]bool, n)
		for j := 0; j < i; j++ {
			words[string(s[j])] = true
		}

		var cnt int
		for j := i; j < n; j++ {
			if val, ok := words[string(s[j])]; ok && val {
				cnt++
				words[string(s[j])] = false
			}
		}

		ans = max(ans, cnt)
	}

	fmt.Println(ans)
}

func StrStdin() string {
	scan.Scan()
	return scan.Text()
}

func NumStdin() int {
	num, err := strconv.Atoi(StrStdin())
	if err != nil {
		panic(err)
	}
	return num
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
