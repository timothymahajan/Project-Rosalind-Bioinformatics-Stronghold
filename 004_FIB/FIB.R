#Problem 4: Rabbits and Recurrence Relations
#Given: Positive integers n≤40n≤40 and k≤5k≤5.
#Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

fibonacci <- function(a1 = 1, a2 = 1, t, k = 1) {
  vec<-vector()
  vec[1]<-a1
  vec[2]<-a2
  for(i in 3:t) {
    vec[i]<-vec[i-1]+k*vec[i-2]
  }
  return(vec)
}

out<-fibonacci(t=31,k=5)

format(out[length(out)])
