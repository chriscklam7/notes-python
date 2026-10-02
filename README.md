# Notes of Python

## Pattern

```python
import packagexyz

class Circle:
    def __init__(self, radius):
        self.PI_6DEC = 3.141592
        self.radius = radius
    
    def circumference(self):
        return 2 * self.PI_6DEC * self.radius
    
    def get_area(self):
        return self.PI_6DEC * self.radius * self.radius


given_radius = 10
circle = Circle(given_radius)
circle_area = circle.get_area()
```

```python
/directory-name/file_name.py
```

<br />

## Conda

<details>
<summary>List environment</summary>

```shell
conda env list
```

</details>

<details>
<summary>Update</summary>

```shell
conda update --all
```

</details>

<details>
<summary>Create environment with specific Python version</summary>

```shell
conda create -n [ENVIRONMENT_NAME] python=[SPECIFIC_PYTHON_VERSION]
```

</details>

<details>
<summary>Create environment with YAML file</summary>

```shell
conda create -n [ENVIRONMENT_NAME] -f [YAML_FILE]
```

</details>

<details>
<summary>Activate environment</summary>

```shell
conda activate [ENVIRONMENT_NAME]
```

</details>

<details>
<summary>Deactivate environment</summary>

```shell
conda deactivate
```

</details>

<details>
<summary>Remove environment</summary>

```shell
conda env remove -n [ENVIRONMENT_NAME]
```

</details>

<details>
<summary>Rename environment</summary>

```shell
conda rename -n [CURRENT_ENVIRONMENT_NAME] [NEW_ENVIRONMENT_NAME]
```

</details>

<br />

## PIP

[https://pypi.org/](https://pypi.org/)

<details>
<summary>Update PIP</summary>

```shell
pip install --upgrade pip
```

</details>

<details>
<summary>Update packages</summary>

```shell
pip list -o | cut -f1 -d' ' | tr " " "\n" | awk '{if(NR>=3)print}' | cut -d' ' -f1 | xargs -n1 pip install -U
```

</details>

<details>
<summary>Export installed Python packages</summary>

```shell
pip freeze > requirements.txt
```

</details>

<details>
<summary>Install Python packages by exported list</summary>

```shell
pip install -r requirements.txt
```

</details>

<br />

## Snippets

[./str_gen.py](String generator)