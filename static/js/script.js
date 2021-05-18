const PROD = true
const BASE_URL = PROD ? 'https://carprc.herokuapp.com/' : 'http://127.0.0.1:5000'

console.log('script working')

const brands = [
    'Honda',
    'Hyundai',
    'Mahindra',
    'Maruti_Suzuki',
    'Renault',
    'Skoda',
    'Tata',
    'Toyota',
    'Volkswagen'
]

const modals = [
    'A-Star' ,
    'Accord' ,
    'Alphard' ,
    'Alto' ,
    'Altroz' ,
    'Alturas' ,
    'Amaze' ,
    'Ameo' ,
    'Aria' ,
    'Aspire' ,
    'BR-V' ,
    'Baleno' ,
    'Beetle' ,
    'Bolero' ,
    'Bolt' ,
    'Brio' ,
    'CR-V' ,
    'Camry' ,
    'Captur' ,
    'Celerio' ,
    'Ciaz' ,
    'City' ,
    'Civic' ,
    'Classic' ,
    'Corolla' ,
    'Creta' ,
    'Cross' ,
    'Duster' ,
    'Dzire' ,
    'EcoSport' ,
    'Eeco' ,
    'Elantra' ,
    'Elite' ,
    'Endeavour' ,
    'Eon' ,
    'Ertiga' ,
    'Estilo' ,
    'Etios' ,
    'Fiesta' ,
    'Figo' ,
    'Fluence' ,
    'Fluidic' ,
    'Fortuner' ,
    'GTI' ,
    'Getz' ,
    'Grand' ,
    'Harrier' ,
    'Hexa' ,
    'Ignis' ,
    'Ikon' ,
    'Indica' ,
    'Indigo' ,
    'Innova' ,
    'Jazz' ,
    'Jetta' ,
    'KUV100' ,
    'Kodiaq' ,
    'Koleos' ,
    'Kona' ,
    'Kwid' ,
    'Land' ,
    'Laura' ,
    'Lodgy' ,
    'Manza' ,
    'Marazzo' ,
    'Mobilio' ,
    'Nano' ,
    'Nexon' ,
    'NuvoSport' ,
    'Octavia' ,
    'Omni' ,
    'Passat' ,
    'Polo' ,
    'Pulse' ,
    'Quanto' ,
    'Rapid' ,
    'Ritz' ,
    'S-Cross' ,
    'SX4' ,
    'Safari' ,
    'Santa' ,
    'Santro' ,
    'Scorpio' ,
    'Sonata' ,
    'Sumo' ,
    'Superb' ,
    'Swift' ,
    'TUV300' ,
    'Thar' ,
    'Tiago' ,
    'Tigor' ,
    'Tiguan' ,
    'Triber' ,
    'Tucson' ,
    'Vento' ,
    'Venue' ,
    'Verna' ,
    'Vitara' ,
    'WR-V' ,
    'Wagon' ,
    'XL6' ,
    'XUV300' ,
    'XUV500' ,
    'Xcent' ,
    'Xylo' ,
    'Yaris' ,
    'Yeti' ,
    'Zen' ,
    'Zest' ,
    'e2o' ,
    'i10' ,
    'i20' ,
]

const pushOptionsToInput = (element_id,data) => {
    const my_input = document.getElementById(element_id)
    for(let i of data){
        const option_el = document.createElement("option")
        option_el.setAttribute('value',i)
        option_el.innerText = i
        console.log(i)
        my_input.appendChild(option_el)
    }
}

pushOptionsToInput('first',brands)
pushOptionsToInput('second',modals)


//get prediction
const predict = async() => {
    try{
      const form_el = document.getElementById('form-el')

        let form = new FormData(form_el)
        // form.append('Company','Honda')
        // form.append('carName','WR-V')
        // form.append('km',763482)
        // form.append('Owner',1)
        // form.append('Age',14)
        // form.append('Fuel_Type_Petrol','Petrol')

        const url = BASE_URL + '/predict'
        const data = await fetch(url,{
            headers:{
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body:new URLSearchParams(form),
            method:'POST',
            mode:'no-cors'
        })
        const json = await data.json()
        //alert(JSON.stringify(json))
        const output_el = document.getElementById('output-message')
        output_el.innerText = json.message

    }catch(err){
        alert(err.message)
    }
}
