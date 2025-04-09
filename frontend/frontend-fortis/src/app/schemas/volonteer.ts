export class Volonteer{
  id:number;
  email:string;
  password:string;
  phonenumbe:string;
  name:string;
  surname:string;
  rating:number
  constructor(
    id:number,
    email:string,
    password:string,
    phonenumbe:string,
    name:string,
    surname:string,
    rating:number,
  ) {
    this.id = id;
    this.email = email;
    this.password = password;
    this.phonenumbe = phonenumbe;
    this.name = name;
    this.surname = surname;
    this.rating = rating
  }
}

