from createApplication import create_app


def main():
    try:
        app = create_app()
        app.run(debug=True,port=5002)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
