const arr = [2,5,1,3,0,10,6,11,13]
const find_element = (element,array)=>{
    for(ele in array){
        if (element==arr[ele]){
            return ele
        }
    }
    return false
}



console.log(find_element(110,arr))