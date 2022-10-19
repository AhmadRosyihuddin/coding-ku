var data = []
function soal1() {
	var x = [10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50]
	hasil = ''
	for (let i = 0 ; i < 21 ; i++){
		hasil += 'Z = 2 * '+x[i]+' + 15 * '+x[i]+' = '+(2*x[i]+15+x[i])+'<br>'
	}
	document.getElementById('demo1').innerHTML = hasil;
}

function sum(total,value){
	return total + value 
}

function mean(){
	var jmlh = data.reduce(sum)
	return jmlh/data.length
}

function modus(){
	if (data.length == 0)
		return null
	var nilai = {}
	var modus = data[0],maxIndex = 1
	for (let i = 0 ; i < data.length; i++){
		key = data[i]
		if(nilai[key] == null)
			nilai[key] = 1
		else
			nilai[key] += 1

		if (nilai[key] > maxIndex) {
			modus = key
			maxIndex = nilai[key]
		}
		
	}
	if (nilai[modus] > 1)
		return modus
	console.log(data.sort())
}


function median(){
	urutData = data.sort()
	hasil = urutData.length / 2
	return urutData[hasil]
}

function soal2() {
	var min = Number(document.getElementById('awal').value);
	var max = Number(document.getElementById('akhir').value);
	data = []
	for (let i = 0 ; i <20; i++){
		nilai = Math.floor(Math.random()* (max - min + 1)) + min;
		data.push(nilai)
	}
	document.getElementById('demo2').innerHTML = 'Data = ['+data+']';
	document.getElementById('min').innerHTML = Math.min.apply(Math,data);
	document.getElementById('max').innerHTML = Math.max.apply(Math,data);
	document.getElementById('mean').innerHTML = mean();
	document.getElementById('modus').innerHTML = modus();
	document.getElementById('median').innerHTML = median();
}
