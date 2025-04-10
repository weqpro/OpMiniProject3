export class Soldier{
  id:number;
  email:string;
  password:string;
  phonenumb:string;
  name:string;
  surname:string;
  battalion:string;
  photo_path:string;
  bio:string;



  constructor(
    id:number,
    email:string,
    password:string,
    phonenumb:string,
    name: string,
    surname:string,
    battalion:string,
    photo_path:string,
    bio:string,
  ){
    this.id = id;
    this.email = email;
    this.password = password;
    this.phonenumb = phonenumb;
    this.name = name;
    this.surname = surname;
    this.battalion = battalion;
    this.photo_path = photo_path;
    this.bio = bio;
  }
}
