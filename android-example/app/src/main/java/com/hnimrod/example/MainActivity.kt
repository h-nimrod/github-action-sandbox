package com.hnimrod.example

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import com.hnimrod.example.ui.theme.AndroidExampleTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            AndroidExampleTheme {
                // A surface container using the 'background' color from the theme
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background,
                ) {
                    Box(contentAlignment = Alignment.Center) {
                        val snackbarHostState = remember { SnackbarHostState() }
                        SnackbarHost(
                            hostState = snackbarHostState,
                            modifier = Modifier.align(Alignment.BottomCenter)
                        )
                        Greeting("Android", snackbarHostState)
                    }
                }
            }
        }
    }
}

@Composable
fun Greeting(name: String, snackbarHostState: SnackbarHostState, modifier: Modifier = Modifier) {
    val text = "Hello $name!"
    val showSnackbar = remember { mutableStateOf(false) }

    Text(
        text = text,
        modifier = modifier.clickable {
            showSnackbar.value = true
        }
    )

    if (showSnackbar.value) {
        LaunchedEffect(snackbarHostState) {
            snackbarHostState.showSnackbar(message = text)
            showSnackbar.value = false
        }
    }
}

@Preview(showBackground = true)
@Composable
fun GreetingPreview() {
    AndroidExampleTheme {
        Greeting("Android", SnackbarHostState())
    }
}
