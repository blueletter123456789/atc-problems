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
	dx := [8]int{0, 1, 1, 1, 0, -1, -1, -1}
	dy := [8]int{-1, -1, 0, 1, 1, 1, 0, -1}

	h := NumStdin()
	w := NumStdin()
	area := make([]string, h)
	for i := range area {
		area[i] = StrStdin()
	}

	ans := make([][]string, h)
	for i := 0; i < h; i++ {
		ans[i] = make([]string, w)
		for j := 0; j < w; j++ {
			if area[i][j] == '#' {
				ans[i][j] = "#"
				continue
			}
			
			var cnt int
			for k := range dx {
				nx, ny := j+dx[k], i+dy[k]
				if nx < 0 || nx >= w || ny < 0 || ny >= h {
					continue
				}
				if area[ny][nx] == '#' {
					cnt++
				}
			}
			ans[i][j] = strconv.Itoa(cnt)
		}
	}

	for i := range ans {
		fmt.Println(strings.Join(ans[i], ""))
	}
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
