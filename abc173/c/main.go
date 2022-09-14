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
	h := NumStdin()
	w := NumStdin()
	k := NumStdin()
	c := make([]string, h)
	for i := range c {
		c[i] = StrStdin()
	}

	var ans int
	for i := 0; i < (1<<h); i++ {
		for j := 0; j < (1<<w); j++ {
			var cnt int
			for n := 0; n < h; n++ {
				for m := 0; m < w; m++ {
					if ((i & (1<<n)) == 0) || ((j & (1<<m)) == 0) {
						continue
					}
					if c[n][m] == '#' {
						cnt++
					}
				}
			}
			if cnt == k {
				ans++
			}
		}
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
