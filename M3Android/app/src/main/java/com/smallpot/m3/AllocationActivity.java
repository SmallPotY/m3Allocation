package com.smallpot.m3;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.KeyEvent;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class AllocationActivity extends AppCompatActivity {

    EditText editOrderId;
    EditText editLocationId;
    EditText editNumber;

    private String order_id;
    private String location_id;
    private int number;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_allocation);


        editOrderId = findViewById(R.id.editOrderId);

        editOrderId.setOnKeyListener(new View.OnKeyListener() {
            @Override
            public boolean onKey(View v, int keyCode, KeyEvent event) {
                if (event.getKeyCode() == KeyEvent.KEYCODE_ENTER) {

                    order_id = editOrderId.getText().toString();
                    if (order_id.equals("")) {
                        Toast.makeText(AllocationActivity.this, "请输入订单号", Toast.LENGTH_SHORT).show();
                        editOrderId.setFocusable(true);
                        return true;
                    }

                    Toast.makeText(AllocationActivity.this, order_id, Toast.LENGTH_SHORT).show();
                    order_id = "";
                    editOrderId.setText("");
                    return true;
                }
                return false;
            }
        });

    }
}
