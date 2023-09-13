import {useState} from 'react';
import axios from 'axios';

export default function LoginPage() {
    const [id, setId] = useState('')
    const [password, setPassword] = useState('')
    const [nickName, setNickName] = useState('')

    const onChangeId = (event)=> {
        setId(event.target.value)
    }

    const onChangePassword = (event) => {
        setPassword(event.target.value)
    }

    const onChangeNickName = (event) => {
        setNickName(event.target.value)
    }

    const onClickSubmit = async () => {
        try{
            const response = await axios.post('http://localhost:8080/user/signup', {
                id,
                password,
                nickName
            })
            console.log(response)

            if (response.status === 200) {
                setNickName('');
                setId('');
                setPassword('');
                alert('축하합니다 회원가입 성공!~')
            }

        }catch(error){
            console.log('Error', error);
        }
    }

    return(
        <>
            아이디 : <input onChange={onChangeId} />
            비밀번호 : <input onChange={onChangePassword} />
            닉네임 : <input onChange={onChangeNickName} />

            <button onClick={onClickSubmit}>전송하기</button>
        </>
    )
}