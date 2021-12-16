import { Statistic, Row, Col, Button } from 'antd';
// import { useState } from 'react';

function MyStats(){

    // const { User, setUser } = useState(null);

    return (
        <div>
            <Row gutter={16}>
                <Col span={12}>
                <Statistic title="Users" value={5} />
                </Col>
                <Col span={12}>
                <div>
                    <Button type="primary">Master</Button>
                    <br />
                    <br />
                    <Button type="primary">Known</Button>
                    <br />
                </div>
                <Button style={{ marginTop: 16 }} type="primary">
                    Configure
                </Button>
                </Col>
                <Col span={12}>
                <Statistic title="Active Users" value={2} loading />
                </Col>
            </Row>
        </div>
    )
}
export default MyStats;