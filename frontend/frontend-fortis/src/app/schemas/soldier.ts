export class Soldier{
  id:number;
  email:string;
  password:string;
  phonenumb:string;
  name:string;
  surname:string;
  unit:string;
  subunit:string;
  battalion:string;


  constructor(
    id:number,
    email:string,
    password:string,
    phonenumb:string,
    name: string,
    surname:string,
    unit:string,
    subunit:string,
    battalion:string,
  ){
    this.id = id;
    this.email = email;
    this.password = password;
    this.phonenumb = phonenumb;
    this.name = name;
    this.surname = surname;
    this.unit = unit;
    this.subunit = subunit;
    this.battalion = battalion;
  }
}
