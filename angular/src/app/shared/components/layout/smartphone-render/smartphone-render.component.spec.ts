import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SmartphoneRenderComponent } from './smartphone-render.component';

describe('SmartphoneRenderComponent', () => {
  let component: SmartphoneRenderComponent;
  let fixture: ComponentFixture<SmartphoneRenderComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SmartphoneRenderComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SmartphoneRenderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('Componente generado correctamente', () => {
    expect(component).toBeTruthy();
  });
});
