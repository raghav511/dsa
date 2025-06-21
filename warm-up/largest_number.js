// const arr = [2,5,1,-1,-1,3,0,10,6,-2,11,13,-3]
const arr = [0]

const largest_num = (array) =>{
    let max = Number.NEGATIVE_INFINITY
    for(element of array){
        if(element>max){
            max=element
        }
    }
    return max
}

console.log(largest_num(arr))
