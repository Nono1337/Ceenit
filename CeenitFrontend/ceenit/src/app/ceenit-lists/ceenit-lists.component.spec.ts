import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CeenitListsComponent } from './ceenit-lists.component';

describe('CeenitListsComponent', () => {
  let component: CeenitListsComponent;
  let fixture: ComponentFixture<CeenitListsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CeenitListsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CeenitListsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
