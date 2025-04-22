export class Volonteer{
  id:number;
  email:string;
  password:string;
  phonenumber:string;
  name:string;
  surname:string;
  photo_path:string;
  bio:string;
  constructor(
    id:number,
    email:string,
    password:string,
    phonenumber:string,
    name:string,
    surname:string,
    photo_path:string,
    bio:string,

  ) {
    this.id = id;
    this.email = email;
    this.password = password;
    this.phonenumber = phonenumber;
    this.name = name;
    this.surname = surname;
    this.photo_path = photo_path;
    this.bio = bio;
  }
}