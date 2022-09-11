package main

import (
	"bufio"
	"fmt"
	"os"
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
	s := StrStdin()
	height := len(s)

	var ans int
	for i := range s {
		if s[i] == 'U' {
			ans += height - (i+1)
			ans += i*2
		} else {
			ans += i
			ans += (height - (i+1)) * 2
		}
	}

	fmt.Println(ans)
}

func StrStdin() string {
	scan.Scan()
	return scan.Text()
}
