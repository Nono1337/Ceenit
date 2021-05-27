import { Component, OnInit } from '@angular/core';
import {MatSort} from '@angular/material/sort';
import {MatTableDataSource} from '@angular/material/table';
import { HttpServiceService } from 'src/app/service/http-service.service';
import { ActivatedRoute } from '@angular/router';
import { MovieList } from '../Model/movie.model';

@Component({
  selector: 'app-ceenit-lists',
  templateUrl: './ceenit-lists.component.html',
  styleUrls: ['./ceenit-lists.component.css']
})
export class CeenitListsComponent implements OnInit {

  constructor() {}
  
  ngOnInit(): void {
    
  }

}
