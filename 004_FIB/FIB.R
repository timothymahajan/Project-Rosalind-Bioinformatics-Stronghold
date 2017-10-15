

fibonacci <- function(a1=1,a2=1,t,k=1) {
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
