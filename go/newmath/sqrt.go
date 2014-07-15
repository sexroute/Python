// Package newmath is a trivial example package 
package newmath
func Sqrt(x float64)float64 {
	z := float64(1)
	for i := 0; i < 1000; i++ {
		z -= (z*z - x) / (2*z)
	}
	return z
}