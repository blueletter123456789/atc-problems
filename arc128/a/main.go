package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
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
	a := make([]int, n)
	for i := range a {
		a[i] = NumStdin()
	}
	da := make([]int, n)
	for i := 1; i < n; i++ {
		da[i] = a[i] - a[i-1]
	}

	ans := make([]string, n)
	for i := range ans {
		ans[i] = "0"
	}
	var flg bool
	for i := n-1; i >= 0; i-- {
		if flg && da[i] >= 0 {
			ans[i] = "1"
			flg = !flg
		} else if !flg && da[i] < 0 {
			ans[i] = "1"
			flg = !flg
		}
	}
	fmt.Println(strings.Join(ans, " "))
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}
