import { Component, OnInit } from '@angular/core';
import { ClientService } from '../client.service';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  list: any;
  

  constructor(private clientService: ClientService) { }

  elaboration(){
    this.clientService.client().subscribe(response => {
      console.log(response)
      this.list = response.result
    })
  }


  ngOnInit(): void {
  }

}


