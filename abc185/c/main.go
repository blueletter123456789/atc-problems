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
	l := NumStdin()
	seen := make([]bool, 11)

	ans := 1
	for i := 1; i <= 11; i++ {
		num := l - i
		for j := 11; j > 1; j-- {
			if num % j == 0 && !seen[j-1] {
				seen[j-1] = true
				num /= j
			}
		}
		ans *= num
	}

	for i, ok := range seen {
		if i != 0 && !ok {
			ans /= (i+1)
		}
	}

	fmt.Println(ans)
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}
